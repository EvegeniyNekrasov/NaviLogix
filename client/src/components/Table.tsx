import React, { useState } from "react";
import {
    useReactTable,
    ColumnDef,
    flexRender,
    getCoreRowModel,
    getFilteredRowModel,
    getPaginationRowModel,
    PaginationState,
} from "@tanstack/react-table";

import {
    ChevronLeft,
    ChevronRight,
    ChevronsLeft,
    ChevronsRight,
} from "lucide-react";

type GenericTableProps<TData extends object> = {
    data: TData[];
};

// TODO: onClick handler to return lat, lon if passed object contains it

function GenericTable<TData extends object>({
    data,
}: GenericTableProps<TData>) {
    const [pagination, setPagination] = React.useState<PaginationState>({
        pageIndex: 0,
        pageSize: 5,
    });
    const [globalFilter, setGlobalFilter] = useState("");

    const columns = React.useMemo<ColumnDef<TData>[]>(
        () =>
            data && data.length > 0
                ? (Object.keys(data[0]) as Array<keyof TData>).map((key) => ({
                      accessorKey: key as string,
                      header: formatHeader(key as string),
                  }))
                : [],
        [data]
    );

    const table = useReactTable({
        data,
        columns,
        state: {
            globalFilter,
            pagination,
        },
        onGlobalFilterChange: setGlobalFilter,
        onPaginationChange: setPagination,
        getCoreRowModel: getCoreRowModel(),
        getFilteredRowModel: getFilteredRowModel(),
        getPaginationRowModel: getPaginationRowModel(),
        globalFilterFn: "auto",
    });

    return (
        <div className="p-6 h-full w-full bg-neutral-100 dark:bg-gray-800 text-black dark:text-white rounded-xl">
            <input
                type="text"
                value={globalFilter.toLowerCase() ?? ""}
                onChange={(e) => setGlobalFilter(e.target.value)}
                placeholder="Buscar..."
                className="mb-4 p-2 border border-gray-300 rounded w-full"
            />

            <table className="min-w-full divide-y divide-gray-200">
                <thead className="bg-gray-50 dark:bg-slate-100">
                    {table.getHeaderGroups().map((headerGroup) => (
                        <tr key={headerGroup.id}>
                            {headerGroup.headers.map((header) => (
                                <th
                                    key={header.id}
                                    className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                                    {flexRender(
                                        header.column.columnDef.header,
                                        header.getContext()
                                    )}
                                </th>
                            ))}
                        </tr>
                    ))}
                </thead>
                <tbody className="bg-white dark:bg-black divide-y divide-gray-200">
                    {table.getRowModel().rows.map((row) => (
                        <tr
                            key={row.id}
                            className="hover:bg-gray-100 hover:dark:bg-slate-900">
                            {row.getVisibleCells().map((cell) => (
                                <td
                                    key={cell.id}
                                    className="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                                    {flexRender(
                                        cell.column.columnDef.cell,
                                        cell.getContext()
                                    )}
                                </td>
                            ))}
                        </tr>
                    ))}
                </tbody>
            </table>

            <div className="mt-4 flex items-center justify-between">
                <div className="flex items-center gap-2">
                    <button
                        className="p-2 border rounded"
                        onClick={() => table.setPageIndex(0)}
                        disabled={!table.getCanPreviousPage()}>
                        <ChevronsLeft />
                    </button>
                    <button
                        className="p-2 border rounded"
                        onClick={() => table.previousPage()}
                        disabled={!table.getCanPreviousPage()}>
                        <ChevronLeft />
                    </button>
                    <button
                        className="p-2 border rounded"
                        onClick={() => table.nextPage()}
                        disabled={!table.getCanNextPage()}>
                        <ChevronRight />
                    </button>
                    <button
                        className="p-2 border rounded"
                        onClick={() =>
                            table.setPageIndex(table.getPageCount() - 1)
                        }
                        disabled={!table.getCanNextPage()}>
                        <ChevronsRight />
                    </button>
                    <span>
                        Página{" "}
                        <strong>
                            {table.getState().pagination.pageIndex + 1} de{" "}
                            {table.getPageCount()}
                        </strong>
                    </span>
                </div>
                <div>
                    <select
                        value={table.getState().pagination.pageSize}
                        onChange={(e) => {
                            table.setPageSize(Number(e.target.value));
                        }}
                        className="p-2 border rounded">
                        {[5, 10, 20, 50].map((pageSize) => (
                            <option
                                key={pageSize}
                                value={pageSize}>
                                Mostrar {pageSize}
                            </option>
                        ))}
                    </select>
                </div>
            </div>
        </div>
    );
}

export default GenericTable;

function formatHeader(key: string): string {
    return key
        .replace(/([A-Z])/g, " $1")
        .replace(/^./, (str) => str.toUpperCase());
}
